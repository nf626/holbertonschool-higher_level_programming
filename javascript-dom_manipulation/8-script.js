document.addEventListener('DOMContentLoaded', getData);

async function getData() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        document.getElementById('hello').textContent = json.hello;
    }
    catch (error) {
        console.error(error.message);
    }
}
