# [level 4] [3차] 자동완성 - 17685 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/17685) 

### 성능 요약

메모리: 320 MB, 시간: 1557.21 ms

### 구분

코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<h2 style="user-select: auto;">자동완성</h2>

<p style="user-select: auto;">포털 다음에서 검색어 자동완성 기능을 넣고 싶은 라이언은 한 번 입력된 문자열을 학습해서 다음 입력 때 활용하고 싶어 졌다. 예를 들어, <code style="user-select: auto;">go</code> 가 한 번 입력되었다면, 다음 사용자는 <code style="user-select: auto;">g</code> 만 입력해도 <code style="user-select: auto;">go</code>를 추천해주므로 <code style="user-select: auto;">o</code>를 입력할 필요가 없어진다! 단, 학습에 사용된 단어들 중 앞부분이 같은 경우에는 어쩔 수 없이 다른 문자가 나올 때까지 입력을 해야 한다.<br style="user-select: auto;">
효과가 얼마나 좋을지 알고 싶은 라이언은 학습된 단어들을 찾을 때 몇 글자를 입력해야 하는지 궁금해졌다.</p>

<p style="user-select: auto;">예를 들어, 학습된 단어들이 아래와 같을 때</p>
<div class="highlight" style="user-select: auto;"><pre class="codehilite" style="user-select: auto;"><code style="user-select: auto;">go
gone
guild
</code></pre></div>
<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">go</code>를 찾을 때 <code style="user-select: auto;">go</code>를 모두 입력해야 한다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">gone</code>을 찾을 때 <code style="user-select: auto;">gon</code> 까지 입력해야 한다. 
(<code style="user-select: auto;">gon</code>이 입력되기 전까지는 <code style="user-select: auto;">go</code> 인지 <code style="user-select: auto;">gone</code>인지 확신할 수 없다.)</li>
<li style="user-select: auto;"><code style="user-select: auto;">guild</code>를 찾을 때는 <code style="user-select: auto;">gu</code> 까지만 입력하면 <code style="user-select: auto;">guild</code>가 완성된다.</li>
</ul>

<p style="user-select: auto;">이 경우 총 입력해야 할 문자의 수는 <code style="user-select: auto;">7</code>이다.</p>

<p style="user-select: auto;">라이언을 도와 위와 같이 문자열이 입력으로 주어지면 학습을 시킨 후, 학습된 단어들을 순서대로 찾을 때 몇 개의 문자를 입력하면 되는지 계산하는 프로그램을 만들어보자.</p>

<h3 style="user-select: auto;">입력 형식</h3>

<p style="user-select: auto;">학습과 검색에 사용될 중복 없는 단어 <code style="user-select: auto;">N</code>개가 주어진다. <br style="user-select: auto;">
모든 단어는 알파벳 소문자로 구성되며 단어의 수 <code style="user-select: auto;">N</code>과 단어들의 길이의 총합 <code style="user-select: auto;">L</code>의 범위는 다음과 같다.</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">2 &lt;= <code style="user-select: auto;">N</code> &lt;= 100,000</li>
<li style="user-select: auto;">2 &lt;= <code style="user-select: auto;">L</code> &lt;= 1,000,000</li>
</ul>

<h3 style="user-select: auto;">출력 형식</h3>

<p style="user-select: auto;">단어를 찾을 때 입력해야 할 총 문자수를 리턴한다.</p>

<h3 style="user-select: auto;">입출력 예제</h3>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">words</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">["go","gone","guild"]</td>
<td style="user-select: auto;">7</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">["abc","def","ghi","jklm"]</td>
<td style="user-select: auto;">4</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">["word","war","warrior","world"]</td>
<td style="user-select: auto;">15</td>
</tr>
</tbody>
      </table>
<h3 style="user-select: auto;">입출력 설명</h3>

<ul style="user-select: auto;">
<li style="user-select: auto;">첫 번째 예제는 본문 설명과 같다.</li>
<li style="user-select: auto;">두 번째 예제에서는 모든 단어들이 공통된 부분이 없으므로, 가장 앞글자만 입력하면 된다.</li>
<li style="user-select: auto;">세 번째 예제는 총 <code style="user-select: auto;">15</code> 자를 입력해야 하고 설명은 아래와 같다.

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">word</code>는 <code style="user-select: auto;">word</code>모두 입력해야 한다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">war</code>는 <code style="user-select: auto;">war</code> 까지 모두 입력해야 한다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">warrior</code>는 <code style="user-select: auto;">warr</code> 까지만 입력하면 된다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">world</code>는 <code style="user-select: auto;">worl</code>까지 입력해야 한다. (<code style="user-select: auto;">word</code>와 구분되어야 함을 명심하자)</li>
</ul></li>
</ul>

<p style="user-select: auto;"><a href="http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/" target="_blank" rel="noopener" style="user-select: auto;">해설 보러가기</a></p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges