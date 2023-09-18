from template_tests.pages.template_page import MainPage

main_page = MainPage()


def test_assert_elements_texts():
    main_page.open()

    main_page.assert_banner_text()
    main_page.assert_info_text()
    main_page.assert_partners_text()
