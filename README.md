# 📅 프로젝트 기간

### 💡**아이디어 회의 및 구상**

5월 11일(수) ~ 19일(목)

### 🎨**개발 및 디자인 작업**

5월 20일(금) ~ 26일(목)

---

# 👥 팀원 정보 및 업무 분담 내역

## 👨🏻‍💻 박종민

- Front-End
    - 반응형 웹 구현
    - jQuery, JavaScript, CSS
- Back-End
    - Django

## 👨‍💻 임상빈

- 프로젝트 컨셉 기획, 페이지 구상
- 스케쥴 및 이슈 정리
- Back-End
    - Django
- 디자인
    - 와이어프레임 구상
    - Landing Page 및 Tip Page 제작

---

## 🧬 데이터베이스 모델링 (ERD)

![ERD.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f49f594e-9b83-4123-b061-20c9eb779e69/ERD.jpg)

- 영화 데이터 **TMDB** 사용
- 한 영화가 여러 개의 장르를 가짐 & 장르는 여러 개의 영화에 들어감 → **M:N 관계**
- 한 영화를 여러 사용자가 Like & 한 사용자가 여러 영화를 Like → **M:N 관계**
- 한 영화에 여러 개의 리뷰를 달 수 있음 → **1:N 관계**
- 한 사용자가 여러 개의 리뷰를 쓸수 있음 → **1:N 관계**
- 한 사용자가 여러 개의 댓글을 달 수 있음 → **1:N 관계**
- 한 리뷰(게시글)에는 여러 개의 댓글을 달 수 있음 → **1:N 관계**
- 유저 & 프로필 → **1:1 관계** & **[ 유저는 무조건 존재하지만 프로필은 없거나 한 개만 존재 ]**

---

## 🏁목표 서비스 구현 및 실제 구현 정도

### 🤔 기획의도

‘영화를 언제, 어디서, 어떻게 접하는 경우가 많을까?’ 라는 생각에서 시작된 궁금증이 이 프로젝트의 컨셉으로 정해지게 되었습니다.

집 안에서 생활을 많이 하면서 OTT서비스를 많이 이용하게 되었고, 필요할 때 심심할 때마다 시간을 보내기 위해 영화를 보는 경우가 많습니다.

저희는 집 안에서 벌어지는 일들 중에서 어떤 일이 가장 시간을 많이 보내게 될까? 생각을 했고, `빨래`를 생각하게 되었습니다.

빨래를 분류하고, 세탁기에 넣어 돌리고 탈수 시키고 건조하기까지 오랜 시간 걸리기 때문에 이 시간을 영화와 함께 보낸다면 빨래가 끝나기까지 기다리는 시간이 즐겁지 않을까 생각되어 `빨래 + 영화` 의 조합을 생각하게 되었습니다. 

그리하여 빨래를 위해 빨랫감의 색상을 분류하는 것과 세탁 모드에 포커스를 두어 이용자가 세탁을 돌리는 방식에 따라 영화를 추천하는 `런드리무비`를 기획하게 되었습니다.

## 🥅 목표 서비스

빨래를 하는 사람들의 `세탁 방식을 활용해 다양한 장르의 영화를 추천`하여 새로운 분야나 정보를 접할 수 있도록 영화를 추천하고 이를 `다른 사람들과 후기를 공유하고 소통`할 수 있도록 서비스를 제공하고자 하였습니다.

## 🧑🏻‍⚕️구현 서비스 설계🛠️

### ✍🏻 페이지 스케치

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee87b01e-2af3-4467-9353-3f05f8056556/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0f4ab9a9-a22b-43b7-bf4a-bb66c307b219/Untitled.png)

컨셉을 돋보이게 하면서 처음 사용하는 사용자들도 쉽게 이용할 수 있는 홈페이지와 서비스를 위해 간략하게 스케치를 진행하였습니다.

# 👍 빨랫감 분류와 세탁 모드 활용하여 영화 추천 (알고리즘 활용한 추천 서비스 구현)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bb3f84ed-6f68-4b0f-8dea-ff58ba20b1ef/Untitled.png)

## 구현 전 페이지

💭 처음 설계를 진행할 당시에는 세탁 모드를 많이 분류하여 세분화시키려고 진행했습니다.

💭 세탁기를 사용하는 사람들을 대상으로 인터뷰를 진행해보니 사용하는 모드가 정말 한정적이라는 것을 알아낼 수 있었고, `표준, 쾌속, 이불 또는 삶음` 모드를 이용하기로 결정하였습니다.

💭 색상과 세탁 모드를 결정하면 로직을 거쳐 영화들이 보여질 수 있도록 하였습니다.

## 구현한 페이지

🔨 배경 사진을 뒤에 넣으려고 했으나 기본적으로 흰 배경이 깔끔하게 보인다 판단되어 삽입하지 않았습니다.

🔨 구현 전 페이지에서는 버튼을 누르면 색상이 채워지는 방향으로 구상을 했으나 radio 버튼을 활용하고, radio 선택 버튼을 초기화할 수 있는 버튼을 하단에 두어 다시 선택할 수 있도록 하였습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4344cd67-fdf3-4df2-97a5-8869715a507f/Untitled.png)

🔨 radio 버튼 클릭 시 이벤트가 발생하도록 하여 다른 submit 과정 없이도 추천 영화 목록이 보여질 수 있도록 axios를 사용하였습니다.

🔨 추천으로 뜬 영화 포스터를 호버링하면 포스터가 커지며 클릭하면 각 영화의 세부 페이지로 이동하도록 구현하였습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3a35e03b-ea31-4068-a1ca-d2e36d1a8fec/Untitled.png)

![Screenshot 2022-05-25 at 23.55.34.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a35c25d2-26db-4576-b1e0-aaaa97ba293b/Screenshot_2022-05-25_at_23.55.34.png)

---

# 💬 다른 이용자들과 영화 후기 공유 (커뮤니티 서비스 구현)

## 영화 리뷰 게시판

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/02414c38-1210-4579-a6ad-acd0ab50cff6/Untitled.png)

## 구현 전 페이지

💭 후기를 남길 수 있는 페이지를 만들고 그 안에 카드 형태로 제목과 어떠한 영화에 대한 리뷰인지 알 수 있도록 사진이 띄워질 수 있도록 구상하였습니다.

💭 작성자의 프로필 사진도 게시글 썸네일 자체에 띄우고자 생각하였습니다.

💭 페이지네이션을 구현하여 특정 카드 개수가 차면 다음 페이지로 이동하여 볼 수 있도록 구상하였습니다.

💭 디자인 측면에서 상단에는 특정 배너 구간을 만들어서 공간을 차지하고 게시판은 하단의 3분의 2정도를 차지하도록 설계하였습니다.

## 구현한 페이지

🔨 카드 형태로 어떠한 영화의 리뷰인지 볼 수 있도록 영화의 포스터가 띄워질 수 있도록 하였습니다.

🔨 해당 포스터에 마우스를 호버링하는 경우 리뷰의 제목(한 줄 평)과 작성자, 작성 시간이 띄워지도록 구현하였습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/46f2b22f-e271-4517-8d9a-ea3c684c3191/Untitled.png)

🔨 전체 메뉴의 디자인을 따라하여 배너를 타이포그래피와 이모지만 활용하여 소통하는 느낌을 전달하였습니다.

🔨 기존 ‘세탁 후기’ 로 썼던 메뉴를 직관적으로 ‘영화 후기’로 변경하였습니다.

![영화리뷰.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d2a2aab7-932f-42b7-ac5a-8a85ab1a1396/영화리뷰.png)

### 후기 작성 폼

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0841c20f-f6b2-467c-8b6e-df29e3bbe9a3/Untitled.png)

## 구현 전 페이지

💭 리뷰를 쓰고자하는 영화 제목이 게시판에 자동으로 작성되며, 제목과 유저, 내용을 쓰고 작성할 수 있도록 하였습니다.

💭 리뷰에서 추천과 비추천을 표시할 수 있도록 구상하였습니다.

## 구현한 페이지

🔨 리뷰를 쓰고자하는 영화의 제목이 뜨도록 구현하였습니다

🔨 제목이 아닌 한 줄 평으로 해당 영화의 느낌이나 후기를 남길 수 있도록 하였습니다.

🔨 추천/비추천이 아닌 별점으로 영화에 대한 점수를 매길 수 있도록 하였습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/876fc37f-aa96-48ac-b8b9-c5a3169576b7/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2847436a-7fde-4d06-a309-30b5f0ae531b/Untitled.png)

🔨 별점 작성 시 마우스로 호버링 시 연한 노란색이 채워지다 클릭 시 진한 노란색으로 표현됩니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cadf607b-96ad-4f09-a67e-a9be0e195b2c/Untitled.png)

### 상세 리뷰 페이지

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d5ab1000-7e01-4fda-9053-a28798bc4aee/Untitled.png)

🔨 한 줄 평, 별점, 내용, 작성 일자가 보여질 수 있도록 하였고, 그 아래로는 작성된 댓글과 댓글을 작성할 수 있는 폼이 있습니다.

🔨 리뷰를 작성한 영화의 포스터가 상단에 보여질 수 있도록 하였고, 해당 위치에 마우스를 갖다대면 영화 상세 페이지로 이동할 수 있도록 구현하였습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec03b0cb-3a86-4081-9bdc-e8811e5665ff/Untitled.png)

### 리뷰 수정과 삭제

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/23598095-d3b1-43c0-abc9-d8caef1155f8/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fe6b74d4-e468-4b94-a119-b9390d73c941/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5d5f4d6a-1125-4d26-a573-94f51a54ad77/Untitled.png)

🔨 리뷰 수정은 한 줄 평과 후기가 자동으로 완성되도록 하였고, 별점은 다시 매기는 방식으로 구현하였습니다.

🔨 리뷰 삭제 버튼을 누르면 삭제 알림이 뜨며, 확인 버튼을 누르면 삭제가 되도록 하였습니다.

---

# 🧐 런드리무비의 또 다른 포인트

### 📌 랜딩 페이지

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/191e7404-ba8c-4051-9f7f-ab1efc78d155/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6b8f4ab1-fdef-4db6-88fd-3c9d6af9b0c9/Untitled.png)

로그인을 하지 않은 상태에서 보여지는 런드리무비의 소개 페이지로 스크롤 시 다음 소개 이미지가 등장하며 상단의 로그인과 회원가입 버튼이 따라옵니다.

런드리무비를 이용해보고 싶도록하는 카피와 이미지로 랜딩 페이지를 구상하였습니다.

### 📌 Home 페이지

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c844b70-a52d-4dbd-b82f-12e220895859/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bf96a64-b5e4-4159-8aa4-b6a5d558f3ac/Untitled.png)

처음 로그인 시 마주하는 페이지입니다. 해당 페이지에서는 추천 알고리즘을 거치지 않은 평점이 높은 영화들을 위주로 Carousel을 이용하여 시간이 지나면 자동으로 다른 목록이 보여지도록 구현하였습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3756f5eb-2efb-47b9-8428-4d7332a04939/Untitled.png)

추천 영화 하단에는 방금 올라온 게시글 (후기) 들이 보여지며, 제목과 각 후기에 달린 댓글의 수가 보여집니다.

### 📌 영화 상세 페이지

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1854d717-3045-476d-9add-4a64464826cc/Untitled.png)

영화의 상세(디테일) 페이지입니다.

포스터와 기본 정보들이 보여지며, 제목 옆에 있는 최고 마크를 눌러 영화를 추천한다고 표시할 수 있습니다.

리뷰쓰기 버튼이 있어서 상세페이지에서 바로 영화에 대한 후기를 작성할 수 있습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/968621f5-21ae-433e-8b8f-b8f4ba8d17b9/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b308499c-f7c8-436a-bb1d-6de5e2827fe8/Untitled.png)

영화에 대한 정보 소개 하단에는 관련 영상이 유튜브로 바로 연결되어 보여지며, 그 아래에는 관련된 영화의 포스터들이 보여집니다.

### 📌 빨래TIP 페이지

런드리무비의 컨셉에 맞게 세탁에 대한 꿀팁을 담은 페이지입니다.

만약 우리가 서비스를 실제로 구현한다면? 이라 상상하여 만든 페이지입니다.

매 주 세탁과 빨래에 대한 팁을 업데이트하는 방식으로 만들었습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/835ba82b-ccf1-4597-9181-f0a9dd2fef25/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f99c9213-3a41-4db7-bc21-2dbce4a12ee7/Untitled.png)

### 📌 Navbar 그리고 footer

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b7e3f7cd-a9d8-4eba-9c65-aa02336bf9f8/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aaf47155-f7cf-48a9-9305-a2785432e603/Untitled.png)

Navbar에는 각 페이지로 이동할 수 있는 메뉴와 검색창, 그리고 로그인 되어있는 유저의 이름이 보여지는 프로필 버튼이 구현되어 있습니다.

검색 창에 원하는 영화나 장르, 내용을 입력하면 해당하는 영화들이 보여집니다. `탐정` 입력 시 아래와 같은 결과가 보여집니다.

 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e061d101-a102-429b-b20d-b9c1e11ebe61/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6eac49ed-71a1-4974-afa2-90318ffd7580/Untitled.png)

Footer에는 서비스 구현에 참여한 저희의 이름과 깃허브 주소가 포함되어 있으며, 6반의 상징인 티라노를 활용하여 저작권 표시하였습니다.

### 📌 유저 프로필 페이지

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/daea0a44-93d6-4d62-89a9-ba9ee81f81b7/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9626c3a5-e9e6-4db1-83eb-9e76e8b84047/Untitled.png)

유저 프로필 페이지에는 유저가 직접 프로필 사진을 등록할 수 있도록 하였습니다

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8934d39f-f01f-4d72-b0fa-5d47438eb999/Untitled.png)

또 유저가 작성한 후기와 댓글을 확인할 수 있도록 하였습니다.
