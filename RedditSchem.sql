drop schema public cascade;
create schema public;
CREATE TABLE IF NOT EXISTS POSTS (
	id serial PRIMARY KEY,
        POSTID TEXT,
        SUBREDDIT TEXT,
        SUBREDDITID TEXT,
        AUTHOR TEXT,
        URL TEXT,
        URLDOMAIN TEXT,
        MEDIA TEXT,
        TITLE TEXT,
        SCORE INT,
        DOWNVOTES INT,
        UPVOTES INT,
        COMMENTS INT,
        CREATED BIGINT
);
