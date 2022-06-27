#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models

from product.models import Category


class Product(models.Model):
    vintage = models.PositiveIntegerField(null=True)
    wine_producer = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=20, null=True)
    wine_name = models.CharField(max_length=100, null=True)
    grapes = models.TextField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    category = models.ManyToManyField(Category, blank=True)
    img = models.CharField(max_length=1000, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.wine_name
