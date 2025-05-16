# test.py
import index

def test_user_creation():
    user = index.add_user("TestUser", "guest")
    assert user["name"] == "TestUser"
    print("User creation test passed.")

def test_post_creation():
    post = index.add_post(1, "Title", "Content")
    assert post["title"] == "Title"
    print("Post creation test passed.")

if __name__ == "__main__":
    test_user_creation()
    test_post_creation()
