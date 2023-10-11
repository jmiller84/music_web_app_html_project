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

