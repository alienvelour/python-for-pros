from lesson_03_testing.slug import slugify


def test_slugify_lowercase_and_dashes_spaces() -> None:
    assert slugify("Release Tracker") == "release-tracker"


def test_slugify_strips_outer_whitespace() -> None:
    assert slugify("  Payments API  ") == "payments-api"
