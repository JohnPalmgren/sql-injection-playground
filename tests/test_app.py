from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_album_all_route(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    albums = [
        'Title: Doolittle', 'Released: 1989',
        'Title: Surfer Rosa', 'Released: 1988',
        'Title: Waterloo', 'Released: 1974',
        'Title: Super Trouper', 'Released: 1980',
        'Title: Bossanova', 'Released: 1990',
        'Title: Lover', 'Released: 2019',
        'Title: Folklore', 'Released: 2020',
        'Title: I Put a Spell on You', 'Released: 1965'
    ]
    page.goto(f"http://{test_web_address}/albums")
    divs = page.locator("div")
    expect(divs).to_have_text(albums)


def test_album_all_routes_links(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa album'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Surfer Rosa")

def test_single_album_returns_to_all_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/albums/3")
    link = page.locator("a")
    link.click()
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

def test_album_single_route(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/albums/3")
    title = page.locator("h1")
    release = page.locator("div")
    expect(title).to_have_text('Waterloo')
    expect(release).to_have_text('Released: 1974')

def test_add_new_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add new album")
    page.fill("input[name='title']", "Even in Arcadia")
    page.fill("input[name='release-year']", "2025")
    page.click("input[value='Add album']")
    heading = page.locator("h1")
    div = page.locator("div")
    expect(heading).to_have_text("Even in Arcadia")
    expect(div).to_have_text("Released: 2025")

def test_artists_all_route(page, test_web_address, db_connection):
    db_connection.seed('seeds/artists_table.sql')
    page.goto(f"http://{test_web_address}/artists")
    expect(page.get_by_text("Pixies")).to_be_visible()
    expect(page.get_by_text("ABBA")).to_be_visible()
    expect(page.get_by_text("Taylor Swift")).to_be_visible()
    expect(page.get_by_text("Nina Simone")).to_be_visible()
    expect(page.get_by_text("Rock")).to_be_visible()
    expect(page.get_by_text("Pop").first).to_be_visible()
    expect(page.get_by_text("Jazz")).to_be_visible()

def test_add_new_artist(page, test_web_address, db_connection):
    page.set_default_timeout(1000)
    db_connection.seed('seeds/artists_table.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add new artist")
    page.fill("input[name='name']", "Sleep Token")
    page.fill("input[name='genre']", "Metal")
    page.click("input[value='Add artist']")
    heading = page.locator("h1")
    div = page.locator("div")
    expect(heading).to_have_text("Sleep Token")
    expect(div).to_have_text("Genre: Metal")