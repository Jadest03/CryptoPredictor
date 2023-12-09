# <p align="center">암호화폐 예측 프로그램 📈</p>

<p align="center">
  <img src="/imgs/logo.png" alt="logo">
</p>
<br/><br/>

# <p align="center">프로그램 설명</p>

<p align="center">
  이 파이썬 프로그램은 암호화폐 투자자들을 위한 실용적이고 정확한 예측 도구로서, ARIMA (자기회귀누적이동평균) 시계열 예측 기술을 활용합니다. 이 프로그램은 사용자가 특정한 암호화폐의 이름을 입력하면 웹 스크래핑 기술을 통해 실시간으로 최신 암호화폐 가격 증가율 데이터를 수집하고, 이 데이터를 활용하여 머신러닝 알고리즘을 훈련시켜 가격의 동향을 예측합니다.
  <br/>
  사용자는 직관적인 그래픽 사용자 인터페이스(GUI)를 통해 암호화폐명을 입력하고, 예측 결과를 쉽게 시각화할 수 있습니다. 이 프로그램은 Upbit에서 암호화폐 가격 데이터를 수집하며, ARIMA 모델을 활용하여 3초 후의 암호화폐 성장률을 예측합니다. 동시에 지난 2주간의 입력한 암호화폐의 가격 증가율 데이터 또한 가져와 활용하여 모델을 지속적으로 향상시키고, 정확한 예측 결과를 제공합니다.
</p>

# <p align="center">기능</p>

1. 동적(실시간) 및 정적 데이터 수집: 웹 스크래핑을 사용하여 [Upbit](https://upbit.com/home, "upbit link")에서 지정된 암호화폐의 최신 암호화폐 가격 증가율 데이터와 약 2주간의 가격 증가율 데이터를 가져옵니다. 웹 스크래핑 기술은 selenium 라이브러리 및 Chrome의 가상 드라이버를 이용합니다.
2. ARIMA 시계열 예측: ARIMA 모델을 사용하여 짧은 기간 (3초) 뒤의 암호화폐 성장률을 예측합니다. 데이터가 모일수록, 시간이 지날 수록 더욱 정교하게 3초 후의 암호화폐 가격 증가유을 예측 가능합니다.
3. 사용자 친화적 인터페이스: PyQt5 기반의 그래픽 사용자 인터페이스 (GUI)가 상호 작용 및 시각적으로 매력적인 환경을 제공합니다. 암호화폐명을 입력하는 GUI와 그래프 및 수치 GUI를 제공합니다.
   <br/><br/>

# <p align="center">주의사항</p>

1. 예측 값이 안정화 될 때 까지 기다려야할 수 있습니다. 때문에 초반 예측 값의 변동이 크게 나타날 수 있습니다.
2. 존재하지 않는 암호화폐를 검색 시 노이즈가 발생할 수 있습니다.
3. 암호화폐의 정확한 이름을 입력해야 합니다.
   <br/><br/>

# <p align="center">실행방법</p>

다음과 같은 순서로 프로그램을 실행 가능합니다.

프로그램 파일 가져오기<br/>
`git clone https://github.com/Jadest03/CryptoPredictor`

다운받은 폴더에 파이썬 가상환경 설치<br/>
`python -m venv myenv`

설치한 가상환경 실행<br/>
`.\myenv\Scripts\activate`

pip 최신버전 업그레이드<br/>
`python -m pip install --upgrade pip`

실행하는데 필요한 라이브러리 설치<br/>
`pip install -r requirements.txt`

프로그램 실행<br/>
`절대경로/CryptoPredictor-main/program/thread.py`
<br/><br/>

# <p align="center">실행 후</p>

1. 프로그램 실행 시 입력 GUI가 표시됩니다. </br>
2. 예측 하고 싶은 가상화폐의 정확한 이름을 작성합니다. </br>
3. 그래프 GUI를 통해 값을 확인하고 예측 값을 확인합니다. </br>
   <br/><br/>

# <p align="center">스크린샷</p>

## <p align="center">입력</p>

<p align="center">
  <img src="/imgs/input1.png" alt="input">
</p>
<br/>
<p align="center">
  <img src="/imgs/input2.png" alt="input">
</p>
<br/><br/>

## <p align="center">그래프</p>

<p align="center">
  <img src="/imgs/graph1.png" alt="graph">
</p>

<br/><br/>

# <p align="center">크레딧</p>

<p align="center">✨ 문의 사항이나 궁금한 점에 대해서는 아래 메일로 연락주세요 😄<br/>
    ✨ 개발자 이메일: jadest1018@gmail.com
    <br/><br/>
</p>

# <p align="center">라이센스</p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;이 프로젝트는 MIT LICENSE에 따라 라이센스가 부여됩니다. 자세한 내용은 [라이센스](LICENSE.md)를 참조해주세요. <br/><br/><br/>
