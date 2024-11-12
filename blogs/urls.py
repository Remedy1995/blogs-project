from django.urls import path

from . import views

urlpatterns = [
 path("signup/",views.signup,name="signup"),
 path("login/",views.login,name="login"),
 path("users/",views.fetch_users,name="users"),
 path("create-blogs/",views.makeBLogs,name="blog"),
 path("all-blogs/",views.viewBlogs,name="blogs"),
 path("blogs/<int:id>",views.viewBlogById,name="blog_by_id"),
 path("update-blog/<int:id>",views.updateBlogById,name="update_blog"),
 path("delete-blog/<int:id>",views.deleteBlogById,name="deleteBlog")
]
