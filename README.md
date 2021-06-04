# 자동 약 제공 및 의약품 관리 시스템 Medicine Box

사용자가 안드로이드 앱을 통해 복용해야 하는 약을 정해진 시간에 구급함에서 제공받는 시스템 입니다.

해당 프로젝트는 관리자용 웹, 안드로이드 앱, 스마트 구급함(디바이스), 서버 총 4개의 영역으로 구성되어 있습니다.

#### 기간 : 2020.03.30 ~ 2020.06.24
#### 참여 인원 : 3명
#### 역할 : 팀원
* 서버 : 설계, 구축, 디바이스 인증, 사용자 및 디바이스 관리 기능 개발
* 디바이스 : 설계, 제작, 약 제공, 잔여량 확인, 잔여량 표시, 투입구 잠금, 디바이스 인증, API, WIFI 초기화 기능 개발
* 데이터베이스 : 설계, 구축

---

### 기획

일본 메이지 약학대학 연구팀에 의하면 약 복용을 잊은 경험이 있는 사람이 50.4%로 많은 사람들이 약 복용을 깜빡하고 있습니다. 그 밖에 영양제와 같이 여러 개의 약을 한꺼번에 복용할 때 일일이 꺼내 먹음으로써 약이 오염되는 위험에 노출되고, 보관 중인 의약품을 육안 상으로는 어떤 약인지 구분하기 어려운 경우, 사용 기한을 모르는 의약품을 계속 보관하는 경우로 불안함을 겪고 있습니다.

약은 사람과 아주 가까운 물질로, 가벼이 여겨서도 안 되며 신중한 복용이 필요합니다. 또한 시대가 변화할수록 더더욱 약은 필수적으로 남겨져 도움 받아야 하는 것이고 누구나 필요로 하는 것이므로 이러한 중요성에 합당한 보관법과 사용법이 필요해 보입니다.

따라서 본 프로젝트를 통해 임베디드 시스템을 활용한 자동 약 제공 및 의약품 관리 시스템을 개발하였습니다. 이 시스템을 이용하여 약 복용을 깜빡하는 문제, 과다복용을 하는 문제, 사용기한이 지난 의약품을 보관하는 문제 등을 해소하고자 합니다.

---

### 설계

* 소프트웨어 구성도

![software](https://user-images.githubusercontent.com/62014520/102004738-ab93bd00-3d56-11eb-90d5-243e72936960.png)

* 하드웨어 구성도

![hardware](https://user-images.githubusercontent.com/62014520/102005226-8acd6680-3d5a-11eb-9f93-bbba5e6f0823.png)

* 데이터베이스

![db](https://user-images.githubusercontent.com/62014520/102005484-712d1e80-3d5c-11eb-97e8-c78320be5fa1.png)

---

### 주요 기능 시연

* 약 복용

![play1](https://user-images.githubusercontent.com/62014520/102005404-ea784180-3d5b-11eb-9d59-4b7408e4a246.png)

① 메인 화면에서 복용하기 버튼을 누르면 현재 시간과 오늘 복용하는 약에 설정된 복용 시간을 비교합니다.

② 비교한 시간이 1시간 이내이면 ‘복용 하시겠습니까?’라는 메시지가 뜹니다.

③ 확인을 누르면 디바이스에서 해당 약이 제공됩니다.

* 약 버리기

![plqy2](https://user-images.githubusercontent.com/62014520/102005407-ed733200-3d5b-11eb-928e-a2b98452ed37.png)

① 메인 화면에서 약 버리기 버튼을 누르면 오늘 날짜와 보관 의약품의 사용기한을 비교 합니다.

② 사용기한이 지나지 않았으면 ‘유통기한이 지난 약이 없습니다.’라는 메시지가 뜹니다.

③ 사용기한이 지났다면 ‘약을 버리시겠습니까?’라는 메시지가 뜹니다.

④ 확인을 누르면 해당 의약품이 보관되어 있는 슬롯의 잠금장치가 해제되어 약을 꺼내 버릴 수 있고 해당 약은 보관 의약품 목록에서 삭제됩니다.

* 잔여량 측정

![plqy3](https://user-images.githubusercontent.com/62014520/102005412-efd58c00-3d5b-11eb-8ed9-32790d7b94bc.png)

① 잔여량을 측정 중에는 LED가 여러 색상으로 돌아가고 슬롯의 뚜껑에 부착되어 있는 초음파 센서로 잔여량을 측정합니다.

② 측정이 완료되면 LED의 색상이 약이 매우 적으면 빨간색, 중간 양이면 노란색, 가득 차 있으면 녹색으로 설정됩니다. (사진에서는 모든 공간이 비어있는 상태이므로 모두 빨간색 LED가 들어왔습니다.)

---

### 개발 후기

* 기대 효과

어느 가정에나 구비해두는 구급함이 스마트하게 개발됨에 따라 삶의 질이 높아지고 기획 의도에서 언급한 여러 불편함과 위험성이 감소될 것이라 예상됩니다.

스마트 약통과 같은 기성품과 비교했을 때, 알약 외에도 연고, 밴드 등의 의약품까지도 보관이 가능하다는 차별성을 가지고 있고 약 복용과 관련한 기존 애플리케이션과 비교했을 때, 보관 의약품 정보를 기록해 두는 것뿐만 아니라 디바이스와 연동하여 약 복용, 사용기한 관리를 할 수 있으므로 활용 가치가 좀 더 높을 것으로 기대됩니다.

* 향후 개선 방향

현재 개발된 시스템에서는 한 번 복용한 약을 재복용 하지 못하도록 막아주는 기능이 부재합니다. 이를 개선하면 과다 복용에 대한 해결책이 될 것입니다. 또 인공지능 음성인식 기술을 도입하여 스마트 구급함을 업그레이드하고 기능을 확장 시킨다면 음성으로 약을 제공받거나 복용 확인을 확인할 수 있어 향후 높은 발전 가능성을 보입니다.

---

## Program Stacks
### Web
* Java
* JSP
* HTML
* CSS
* JavaScript
* jQuery
* Bootstrap

### App
* Android 8.0.0 (Oreo)
* Java
* 공공데이터포털 open API

### Device
* Raspberry Pi 4
* Python
* Flask
* Wiring Pi
* Bash

### Server
* JavaScript
* AWS EC2
* AWS RDS
* MariaDB
* Node.js
