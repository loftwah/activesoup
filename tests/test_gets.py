from activesoup import driver


def test_can_get_something(localwebserver):
    d = driver.Driver()
    d.get(f'http://localhost:{localwebserver.port}/foo')


def test_can_decodes_html_into_bs_like_api_document(localwebserver):
    d = driver.Driver()
    page = d.get(f'http://localhost:{localwebserver.port}/html/simple_page.html')
    page_text = page.body.p.text()
    assert page_text == 'text-in-body'
