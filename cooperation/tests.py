from calendar import c
from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        # 1.1 포스트 목록 페이지 가져온다
        response = self.client.get('/cooperation/')
        # 1.2 정상적으로 페이지가 로드된다
        self.assertEqual(response.status_code, 200)
        # 1.3 페이지 타이틀이 'Cooperation'이다
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Cooperation')
        # 1.4 네비게이션 바가 있다.
        # navbar = soup.nav
        # 1.5 다른 페이지로 이동하는 문구가 내비게이션 바에 있다
        # self.assertIn('', navbar.text)

        # 2.1 메인 영역에 게시물이 하나도 없다면
        self.assertEqual(Post.objects.count(), 0)
        # 2.2 '아직 게시물이 없습니다' 라는 문구가 보인다
        main_are = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다', main_area.text)

        # 3.1 게시물이 2개 있다면
        
        # 3.2 포스트 목록 페이지를 새로고침했을 때
        # 3.3 메인 영역에 포스트 2개의 타이틀이 존재한다
        # 3.4 '아직 게시물이 없습니다' 라는 문구는 더 이상 보이지 않는다