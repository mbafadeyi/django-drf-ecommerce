import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act ('data', the variable name, can be anything.)
        data = category_factory(name="test_cat")
        # Assert
        assert data.__str__() == "test_cat"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act ('data', the variable name, can be anything.)
        data = brand_factory(name="test_brand")
        # Assert
        assert data.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act ('data', the variable name, can be anything.)
        data = product_factory(name="test_product")
        # Assert
        assert data.__str__() == "test_product"
