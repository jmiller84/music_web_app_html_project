from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f'http://{test_web_address}/albums')
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Title: Legend\nReleased: 1984",
        "Title: Moonwalker\nReleased: 1990",
        "Title: Bad\nReleased: 1993",
    ])

"""
When we make a get request with an album_id 
We return a single album
"""
def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text(["Album: Legend"])

    p_tag = page.locator('p')
    expect(p_tag).to_have_text(["\nRelease year: 1984\nArtist: Pixies\n"])


"""
When we click an album on GET /albums
We are transfered to the page for that single album 
"""
def test_link_from_albums_to_single_album_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Legend'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text(["Album: Legend"])



"""
When we visit /artists/1 
we return a html page with details for a single artist
"""
def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text(["Artist: Pixies"])

    p_tag = page.locator('p')
    expect(p_tag).to_have_text(["\nGenre: Indie"])

"""
When we visit /artists we see a html page with a list of all artists
The page should contain links to each artists individual artist page
"""
def test_link_from_artists_to_single_artist_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text(["Artist: Pixies"])

"""
When we create a new album 
It appears in the list of albums
"""
def test_create_new_album_using_form(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")

    page.fill("input[name=title]", "Test Album")
    page.fill("input[name=release_year]", "2023")
    page.fill("input[name=artist_id]", "1")

    page.click("text='Add Album'")
    title_tag = page.locator(".t-title")
    expect(title_tag).to_have_text("Album: Test Album")
    release_year_tag = page.locator(".t-release_year")
    expect(release_year_tag).to_have_text("Release year: 2023")
    artist_id_tag = page.locator(".t-artist_id")
    expect(artist_id_tag).to_have_text("Artist ID: 1")

"""
When we create an album withouth passing a title, release_year or artist_id
Then the form shows some errors
"""
def test_create_album_with_errors(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add new album'")
    page.click("text='Add Album'")

    errors_tag = page.locator(".t-errors")
    expect(errors_tag).to_have_text("Your form contained errors: Title can't be blank, Release Year can't be blank, Artist ID can't be blank")
     

"""
When we create a new artist using a html form
We see the new artist listed on the artists page
"""
def test_create_new_artist_from_form(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/music_web_app.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add new artist'") # test that there is a button with the text 'Add new artist'

    page.fill("input[name=name]", "Test Artist") 
    page.fill("input[name=genre]", "Pop")

    page.click("text='Add Artist'")
