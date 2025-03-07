-- lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
WHERE tv_shows.genre_id > 0
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
