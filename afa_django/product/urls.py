from django.urls import include, path
from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('latest-collections/', views.LatestCollectionsList.as_view()),
    path ('products/<slug:collection_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path ('collections/<slug:collection_slug>/', views.CollectionDetails.as_view()),
    path ('collections/<slug:collection_slug>/all', views.CollectionProducts.as_view()),
    path('collections/', views.CollectionsList.as_view()),
    ]