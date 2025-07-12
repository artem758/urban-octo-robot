def generate_reply(message: str) -> str:
    lowered = message.lower()

    if "кто ты" in lowered or "ты бот" in lowered:
        return "Я, типа, цифровой собеседник. Не человек, но и не скучный 🤙"

    if "привет" in lowered:
        return "Йо! Как жизнь? 👋"
    elif "помощь" in lowered:
        return "Спрашивай, не стесняйся. Я тут, чтобы пообщаться 🧠"
    elif "что ты умеешь" in lowered:
        return "Болтать, думать и удивлять. Ну и немного подбросить инфы по VRX 😉"

    return "Хм... звучит интересно. Расскажи ещё 🔍" 