const API_URL = "";

async function authenticate() {
    const initData = window.Telegram?.WebApp?.initData || "";

    console.log(
        "Telegram initData available:",
        Boolean(initData)
    );

    if (!initData) {
        throw new Error(
            "Telegram authentication data отсутствует." +
            "Открой игру через Telegram."
        )
    }

    const response = await fetch(
        `${API_URL}/api/auth/telegram`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                init_data: initData
            })
        }
    );

    const responseText = await response.text();

    console.log(
        "Auth HTTP status:",
        response.status
    );

    console.log(
        "Auth response:",
        responseText
    );

    if (!response.ok) {
        throw new Error(
            `Authentication failed: HTTP ${response.status} — ${responseText}`
        );
    }

    return JSON.parse(responseText);
}

async function getCharacter(characterId) {
    const response = await fetch(
        `${API_URL}/api/character/${characterId}`
    );

    const responseText = await response.text();

    if (!response.ok) {
        throw new Error(
            `Character loading failed: HTTP ${response.status} — ${responseText}`
        );
    }

    return JSON.parse(responseText);
}