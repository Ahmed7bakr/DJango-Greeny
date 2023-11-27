from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
FLAG_OPTION = (("New", "New"), ("Feature", "Feature"), ("Sale", "Sale"))


class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    subtitle = models.CharField(_("Subtitle"), max_length=500)
    sku = models.IntegerField(_("Sku"))
    desc = models.TextField(_("Description"), max_length=10000)
    price = models.FloatField(_("Price"))
    image = models.ImageField(_("Image"), upload_to="products/")
    flag = models.CharField(_("Flag"), max_length=10, choices=FLAG_OPTION)
    quantity = models.IntegerField(_("Quantity"))
    brand = models.ForeignKey(
        "Brand",
        related_name="product_brand",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "Category",
        related_name="product_category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tags = TaggableManager()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class ProductImages(models.Model):
    product = models.ForeignKey(
        Product, related_name="product_image", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return str(self.product)


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to="brands/")
    category = models.ForeignKey(
        "Category",
        related_name="brand_category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    image = models.ImageField(_("Image"), upload_to="categorys/")

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    user = models.ForeignKey(
        User, related_name="user_review", verbose_name="User", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name="product_review",
        verbose_name="Product",
        on_delete=models.CASCADE,
    )
    rate = models.IntegerField(
        _("Rate"), validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    review = models.TextField(_("Review"), max_length=500)
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)

    def __str__(self):
        return str(self.user)
