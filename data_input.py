
from model      import WestaDao
from sqlalchemy import text


def setup_test_data(database):
    new_posts = [{
        'id': 1,
        'img': 'https://scontent-gmp1-1.cdninstagram.com/vp/236ee9845cd1052b5ede2af90689ea8b/5E3D302B/t51.2885-15/sh0.08/e35/s640x640/58410837_2294357490683490_1995145092515161063_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=106 640w,https://scontent-gmp1-1.cdninstagram.com/vp/67b2248b80c42b93605e2aa749ea45af/5E3093EF/t51.2885-15/sh0.08/e35/s750x750/58410837_2294357490683490_1995145092515161063_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=106 750w,https://scontent-gmp1-1.cdninstagram.com/vp/2a10c2eca0b943448a994c7080786e51/5E19C5EF/t51.2885-15/e35/s1080x1080/58410837_2294357490683490_1995145092515161063_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=106 1080w',
        'post_text': '위코드의 모든 커리큘럼은 글로벌 코워킹 스페이스 #wework 에서 진행됩니다.',
        'total_like': 63,
        'author': 'wecode_bootcamp'
    },{
        'id': 2,
        'img': 'https://scontent-gmp1-1.cdninstagram.com/vp/6f773632762191105093909353e83c4b/5E3B5C56/t51.2885-15/sh0.08/e35/s640x640/67415440_525074608253260_6147130801562027883_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=104 640w,https://scontent-gmp1-1.cdninstagram.com/vp/78163ea210d1afea2d3a116d7fff8ebe/5E2E4456/t51.2885-15/sh0.08/e35/s750x750/67415440_525074608253260_6147130801562027883_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=104 750w,https://scontent-gmp1-1.cdninstagram.com/vp/b68e6820398d1c6ee162d016e8da9c66/5E20E2E1/t51.2885-15/e35/s1080x1080/67415440_525074608253260_6147130801562027883_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=104 1080w',
        'post_text': '위코드 2기 수료식! 모두 수고하셨습니다!',
        'total_like': 51,
        'author': 'wecode_bootcamp'
    },{
        'id': 3,
        'img': 'https://scontent-gmp1-1.cdninstagram.com/vp/7e887feffa673df5e0d27bfa90fa6148/5E2A252F/t51.2885-15/sh0.08/e35/p640x640/66710303_674722113002527_2823296399337308947_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=107 640w,https://scontent-gmp1-1.cdninstagram.com/vp/b84c8d804571665579e108cba5a534b2/5E1B372F/t51.2885-15/sh0.08/e35/p750x750/66710303_674722113002527_2823296399337308947_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=107 750w,https://scontent-gmp1-1.cdninstagram.com/vp/4df1fca4a75d6efcf1b2c45e59d92d7c/5E24C8CA/t51.2885-15/e35/p1080x1080/66710303_674722113002527_2823296399337308947_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=107 1080w',
        'post_text': '코딩 중에 간식 챙기는 것은 기본!',
        'total_like': 39,
        'author': 'wecode_bootcamp'
    },{
        'id': 4,
        'img': 'https://scontent-gmp1-1.cdninstagram.com/vp/ba4fcc7c4d4e481ed3e0b64670db41d1/5E222C74/t51.2885-15/sh0.08/e35/s640x640/67752580_2251982321577164_7584410942453240704_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=108 640w,https://scontent-gmp1-1.cdninstagram.com/vp/ebcb4da772e3d3114668d71e3a144596/5E24C9B0/t51.2885-15/sh0.08/e35/s750x750/67752580_2251982321577164_7584410942453240704_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=108 750w,https://scontent-gmp1-1.cdninstagram.com/vp/cc9bd1ff0187fdeda39ab90825f9524b/5E2DC9B0/t51.2885-15/e35/s1080x1080/67752580_2251982321577164_7584410942453240704_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=108 1080w',
        'post_text': '클라이밍을 비롯한 위워크의 다양한 이벤트를 즐길 수 있어요!',
        'total_like': 26,
        'author': 'wecode_bootcamp'
    },{
        'id': 5,
        'img': 'https://scontent-gmp1-1.cdninstagram.com/vp/a6fa26072b6ea9961778bb9d70ed9b87/5E1E8425/t51.2885-15/sh0.08/e35/s640x640/68801638_182495849449265_8439247336083662841_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=105 640w,https://scontent-gmp1-1.cdninstagram.com/vp/8471888c3188ea1bdc176381769bb8dd/5E322825/t51.2885-15/sh0.08/e35/s750x750/68801638_182495849449265_8439247336083662841_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=105 750w,https://scontent-gmp1-1.cdninstagram.com/vp/bd1cd0ab844f96c8d191ffc9d14d0372/5E18A7C0/t51.2885-15/e35/68801638_182495849449265_8439247336083662841_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=105 1080w',
        'post_text': '위코드 프론트엔드 어벤져스!',
        'total_like': 11,
        'author': 'wecode_bootcamp'
    },{
        'id': 6,
        'img': 'https://t1.daumcdn.net/cfile/tistory/99DDFB3B5B42C58522',
        'post_text': '여기가 그 핫하다는 위코드인가요?',
        'total_like': 1,
        'author': '개그맨 황모씨'
    }]


    new_reviews = [{
        'id': 1,
        'review_text': '참 좋은 글이네요.',
        'post_id': 1,
        'author': '행인'
    },{
        'id': 2,
        'review_text': '위워크 넘나 이쁘네요!',
        'post_id': 1,
        'author': '위워크 매니저'
    },{
        'id': 3,
        'review_text': '맥주 맛있겠다...',
        'post_id': 1,
        'author': '그라가스'
    },{
        'id': 4,
        'review_text': '동료 개발자가 되신 것을 축하드립니다.',
        'post_id': 2,
        'author': '갓예리'
    },{
        'id': 5,
        'review_text': '모두 수고많으셨어요~! 축하합니다!',
        'post_id': 2,
        'author': '위코드'
    },{
        'id': 6,
        'review_text': '당분은 정의다.',
        'post_id': 3,
        'author': '당 떨어진 형주'
    },{
        'id': 7,
        'review_text': '선릉2호점만의 특별한 매력!',
        'post_id': 4,
        'author': '위XX 매니저'
    },{
        'id': 8,
        'review_text': '재밌엉...',
        'post_id': 5,
        'author': '왼쪽 사람'
    },{
        'id': 9,
        'review_text': '아 좀만 더 하면 될것 같은데...',
        'post_id': 5,
        'author': '가운데 사람'
    },{
        'id': 10,
        'review_text': '여름엔 춥고 겨울엔 더운 위워크...',
        'post_id': 5,
        'author': '오른쪽 사람'
    },{
        'id': 11,
        'review_text': '하하하하하하하하하',
        'post_id': 6,
        'author': '관객'
    }]
    
