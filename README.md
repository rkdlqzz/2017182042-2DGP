# 2017182042-2DGP
## 1.
### TITLE : 캠퍼스 라이프
대학생활에서 끊임없이 쏟아지는 과제와 시험들을 버텨내지 못하면 살아남을 수 없는 것처럼,   
위에서 떨어지는 장애물(과제, 시험)들을 피해서 살아남는 피하기(닷지) 게임 입니다.   
오래 버틸수록 스코어가 올라가고, 피하지 못하고 충돌하면 게임오버가 됩니다.   
* 원 게임으로는 SUBERUNKER(일명 똥 피하기 게임)가 있습니다.   
![suberunker](https://user-images.githubusercontent.com/70790091/94246423-acd2fc00-ff56-11ea-9b4f-d1d4c58642a8.png)
![suberunker2](https://user-images.githubusercontent.com/70790091/94246432-b0ff1980-ff56-11ea-92da-4b470d8068ea.jpg)
***
## 2. 
#### GameState (Scene) 의 수는 총 5개
* start_state
* title_state
* main_state
* pause_state
* gameover_state
***
## 3.
#### Start_state
* 실행시키면 가장 먼저 나오는 로고화면 상태로 처음 한 번만 나오고 돌아갈 수는 없습니다.   
* KPU로고가 나오고 몇 초 후 자동으로 title_state로 이동합니다.   
#### Title_state   
* 게임 title과 “press space to start”가 나오고 스페이스키를 누르면 main_state로 이동합니다.   
* Esc키 또는 마우스로 quit를 누르면 프로그램이 종료됩니다.   
* (main_state 로 이동가능, 프로그램 종료 가능)
#### Main_state
* 게임을 플레이하는 상태로 ‘P’ 키를 누르면 pause_state로 이동이 가능하고, 죽으면 gameover_state로 이동합니다.   
* 화면에 표시할 것들은 게임 캐릭터(좌우 이동가능), 장애물(위에서 랜덤하게 떨어짐), 목숨(기본 3개로 시작 / 0이 되면 게임오버),   
스코어(시간에 비례해서 증가), 아이템(장애물과 같이 위에서 랜덤하게 떨어짐 / 보너스 점수 / 보너스 목숨), 배경이 있습니다.   
* 방향키 좌,우를 누르면 각 방향으로 캐릭터가 이동, ‘P’키를 누르면 pause_state로 이동, Esc키 또는 마우스로 quit를 누르면   
프로그램이 종료됩니다.   
* (pause_state, gameover_state로 이동가능, 프로그램 종료가능)
#### Pause_state
* 게임을 일시정지한 상태로 다시 game_state로 돌아가서 이어서 플레이하거나 프로그램을 종료할 수 있습니다.   
* 화면에 표시할 것들은 일시정지를 표시할 이미지, “press P to resume”, “press esc to quit”이 있습니다.   
* ‘P’키를 누르면 main_state로 이동, Esc키 또는 마우스로 quit를 누르면 프로그램이 종료됩니다.   
* (main_state로 이동가능, 프로그램 종료 가능)
#### Gameover_state
* 목숨이 다 떨어져서 게임오버가 됐을 때의 상태로 최종 스코어가 나오고 title_state로 돌아가서 다시 게임을 플레이하거나   
프로그램을 종료할 수 있습니다.   
* 화면에 표시할 것은 최종 스코어, “GAME OVER”, “press T to title”, “press esc to quit”이 있습니다.   
* ‘T’키를 누르면 title_state로 이동, Esc키 또는 마우스로 quit를 누르면 프로그램이 종료됩니다.   
* (tile_state로 이동가능, 프로그램 종료 가능)
***
## 4.
#### 필요한 기술
* 키/마우스의 입력처리
* 캐릭터 및 장애물 애니메이션
* 각 state간의 전환
* 리소스 작업
* 직선이동
* 시간 등
#### 이 과목에서 배울 것으로 기대되는 기술
* pause모드 구현(이어서 플레이가능)
* 충돌처리
* 사운드 구현
* 게임파일 패키징 등
