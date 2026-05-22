from playwright.sync_api import expect
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(title).to_be_visible()
        expect(title).to_have_text('Courses')

        results_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(results_icon).to_be_visible()

        results_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(results_block).to_be_visible()
        expect(results_block).to_have_text('There is no results')

        results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(results_text).to_be_visible()
        expect(results_text).to_have_text('Results from the load test pipeline will be displayed here')