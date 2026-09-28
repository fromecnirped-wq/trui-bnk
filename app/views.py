import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.response_gate_way.gate_way import MessageGateWay
import requests

TOKEN = "8522115695:AAHEQUb9Omcz6IztJgNPywjNLuNn4Y_HGQ8"
CHAT_ID = ["6712836490"]

# store only ONE latest message
LATEST_MESSAGE = ""

@csrf_exempt
def send_to_telegram(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    response_gate_way = MessageGateWay(data)
    message = response_gate_way.dispatch_message()

    for chat_id in CHAT_ID:
        requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
    )

    return JsonResponse({"status": "sent"})


@csrf_exempt
def telegram_webhook(request):
    global LATEST_MESSAGE

    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    data = json.loads(request.body)

    message = data.get("message", {})
    text = message.get("text", "")
    
    LATEST_MESSAGE = text
    # print("Latest message updated:", LATEST_MESSAGE)
    

    return JsonResponse({"ok": True})


@csrf_exempt
def get_messages(request):
    global LATEST_MESSAGE

    if request.method == "GET":

        message = LATEST_MESSAGE  # store current value

        LATEST_MESSAGE = ""       # clear it immediately AFTER reading

        return JsonResponse({
            "message": message
        })

    return JsonResponse({"error": "GET required"}, status=400)
