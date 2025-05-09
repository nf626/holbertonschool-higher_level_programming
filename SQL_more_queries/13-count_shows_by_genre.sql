-- lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.
SELECT tv_genres.name AS genre,
COUNT(*) number_of_shows
FROM tv_show_genres
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP by tv_genres.name
ORDER BY number_of_shows DESC;
