# Picturesque-Django-Backend

Picturesque is a tongue-in-cheek name for a social networking app made for sharing photos from a smartphone. Similar to Facebook or Twitter, everyone who creates a new account has a profile and a news feed. When you post a photo on Picturesque, it will be displayed on your profile. It was created to capture special moments and share it with all the other users that you choose.

The website runs its frontend using languages such as HTML5 and CSS3. Bootstrap is used for responsiveness & jQuery for validation and AJAX calls, along with JavaScript. Backend development is done using Python on the Django framework. 

## Methodology

* The Home Page displays posts from all the other users the current user follows. These posts are ordered by recently uploaded posts first. Infinite Scrolling has been implemented to take off load from querying and displaying 100s of posts at a time and provide users a better experience. The user can like the post by clicking the heart button or view the comments of the posts by clicking on the post. To visit the author’s profile page, the user clicks on the username of the author.

* The Profile Page displays a user’s information i.e. their Full Name, Username, Bio, Profile Picture. It also displays all the posts published by this author in tile format which soothes the eye. The user will only be able to see these posts if he is following the user or if he is viewing his on profile. A user can perform various other tasks like send a follow request, cancel the request, un-follow a user from this page. He can visit the Update Profile Page from his own profile page by clicking on the button.

* The Upload Page is a place from where you can publish new posts.

* The Post Details page displays the post photo, number of likes on it, its caption, along with any and all comments that users have made on that particular post.
