document.addEventListener('DOMContentLoaded', getData);

async function getData() {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    const movie_list = document.getElementById('list_movies');

    try {
        const response = await fetch(url); // wait to load url
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

    const json = await response.json(); // return promise and json

    json.results.forEach(movie => {
        const new_element = document.createElement('li');
        new_element.textContent = movie.title;
        movie_list.appendChild(new_element);
    });

    } catch (error) {
        console.error(error.message);
    }
}
