# [level 0] 외계어 사전 - 120869 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120869?language=python3) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴 배열 <code style="user-select: auto;">spell</code>과 외계어 사전 <code style="user-select: auto;">dic</code>이 매개변수로 주어집니다. <code style="user-select: auto;">spell</code>에 담긴 알파벳을 한번씩만 모두 사용한 단어가 <code style="user-select: auto;">dic</code>에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">spell</code>과 <code style="user-select: auto;">dic</code>의 원소는 알파벳 소문자로만 이루어져있습니다.</li>
<li style="user-select: auto;">2 ≤ <code style="user-select: auto;">spell</code>의 크기 ≤ 10</li>
<li style="user-select: auto;"><code style="user-select: auto;">spell</code>의 원소의 길이는 1입니다.</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">dic</code>의 크기 ≤ 10</li>
<li style="user-select: auto;">1 ≤ <code style="user-select: auto;">dic</code>의 원소의 길이 ≤ 10</li>
<li style="user-select: auto;"><code style="user-select: auto;">spell</code>의 원소를 모두 사용해 단어를 만들어야 합니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">spell</code>의 원소를 모두 사용해 만들 수 있는 단어는 <code style="user-select: auto;">dic</code>에 두 개 이상 존재하지 않습니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">dic</code>과 <code style="user-select: auto;">spell</code> 모두 중복된 원소를 갖지 않습니다.</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">spell</th>
<th style="user-select: auto;">dic</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">["p", "o", "s"]</td>
<td style="user-select: auto;">["sod", "eocd", "qixm", "adio", "soo"]</td>
<td style="user-select: auto;">2</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">["z", "d", "x"]</td>
<td style="user-select: auto;">["def", "dww", "dzx", "loveaw"]</td>
<td style="user-select: auto;">1</td>
</tr>
<tr style="user-select: auto;">
<td style="user-select: auto;">["s", "o", "m", "d"]</td>
<td style="user-select: auto;">["moos", "dzx", "smm", "sunmmo", "som"]</td>
<td style="user-select: auto;">2</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"p", "o", "s" 를 조합해 만들 수 있는 단어가 <code style="user-select: auto;">dic</code>에 존재하지 않습니다. 따라서 2를 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #2</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"z", "d", "x" 를 조합해 만들 수 있는 단어 "dzx"가 <code style="user-select: auto;">dic</code>에 존재합니다. 따라서 1을 return합니다.</li>
</ul>

<p style="user-select: auto;">입출력 예 #3</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">"s", "o", "m", "d" 를 조합해 만들 수 있는 단어가 <code style="user-select: auto;">dic</code>에 존재하지 않습니다. 따라서 2을 return합니다.</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">유의사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">입출력 예 #3 에서 "moos", "smm", "som"도 "s", "o", "m", "d" 를 조합해 만들 수 있지만 <code style="user-select: auto;">spell</code>의 원소를 모두 사용해야 하기 때문에 정답이 아닙니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges