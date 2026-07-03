import pytest
from playwright.sync_api import Page, expect

def test_wiki(page: Page):
    page.goto('https://ru.wikipedia.org/')
    page.locator('#ca-talk').get_by_role('link', name='Обсуждение').click()
    expect(page.locator('#firstHeading').get_by_text('Обсуждение' and 'Заглавная страница')).to_be_visible()

@pytest.mark.ui
def test_searh(page: Page):
    page.goto('https://ru.wikipedia.org/')
    page.locator('#searchInput').first.fill('python')
    page.get_by_role('option').first.click()
    expect(page.locator('#firstHeading')).to_have_text('Python')




