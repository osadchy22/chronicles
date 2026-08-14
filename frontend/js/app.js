const tg = window.Telegram.WebApp;

tg.ready();
tg.expand();

async function testApi() {
    try {
        const response = await fetch("api/test");

        const data = await response.json();

        console.log("API TEST SUCCESS:", data);
    }

    catch (error) {
        console.error("API TEST FAILED:", error);
    }
}

testApi();

async function start() {
    const app = document.getElementById("app");

    try {
        console.log("Telegram object:", tg);
        console.log("Telegram initData:", tg.initData);

        const auth = await authenticate();

        console.log("Authentication result:", auth);

        const character = await getCharacter(
            auth.character_id
        );

        console.log("Character:", character);

        renderCharacter(character);

    } catch (error) {
        console.error("GAME ERROR:", error);

        app.innerHTML = `
            <div class="error">
                <h2>Ошибка загрузки</h2>
                <p>${escapeHtml(error.message)}</p>
            </div>
        `;
    }
}

function renderCharacter(character) {
    const app = document.getElementById("app");

    app.innerHTML = `
        <main class="game">

            <header class="header">
                <h1>Chronicles</h1>
            </header>

            <section class="character-card">

                <h2>
                    ${escapeHtml(character.name)}
                </h2>

                <div class="level">
                    Уровень ${character.level}
                </div>

                <div class="resource">
                    ❤️
                    ${character.hp}/${character.max_hp}
                </div>

                <div class="resource">
                    ⚡
                    ${character.energy}/${character.max_energy}
                </div>

                <div class="resource">
                    💰
                    ${character.gold}
                </div>

            </section>

            <button class="primary">
                🗺 Начать исследование
            </button>

        </main>
    `;
}

function escapeHtml(value) {
    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "'");
}

start();