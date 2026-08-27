from lesson_03_testing.slug import slugify


def test_slugify_lowercase_and_dashes_spaces():
    assert slugify("Release Tracker") == "release-tracker"


def test_slugify_strips_outer_whitespace():
    assert slugify("  Payments API  ") == "payments-api"
