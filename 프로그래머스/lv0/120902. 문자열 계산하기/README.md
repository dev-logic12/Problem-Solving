# [level 0] 문자열 계산하기 - 120902 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120902) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;"><code style="user-select: auto;">my_string</code>은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 <code style="user-select: auto;">my_string</code>이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">제한사항</h5>

<ul style="user-select: auto;">
<li style="user-select: auto;">연산자는 +, -만 존재합니다.</li>
<li style="user-select: auto;">문자열의 시작과 끝에는 공백이 없습니다.</li>
<li style="user-select: auto;">0으로 시작하는 숫자는 주어지지 않습니다.</li>
<li style="user-select: auto;">잘못된 수식은 주어지지 않습니다.</li>
<li style="user-select: auto;">5 ≤ <code style="user-select: auto;">my_string</code>의 길이 ≤ 100</li>
<li style="user-select: auto;"><code style="user-select: auto;">my_string</code>을&nbsp;계산한 결과값은 1 이상 100,000 이하입니다.

<ul style="user-select: auto;">
<li style="user-select: auto;"><code style="user-select: auto;">my_string</code>의 중간 계산 값은 -100,000 이상 100,000 이하입니다.</li>
<li style="user-select: auto;">계산에 사용하는 숫자는 1 이상 20,000 이하인 자연수입니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">my_string</code>에는 연산자가 적어도 하나 포함되어 있습니다.</li>
</ul></li>
<li style="user-select: auto;">return type 은 정수형입니다.</li>
<li style="user-select: auto;"><code style="user-select: auto;">my_string</code>의 숫자와 연산자는 공백 하나로 구분되어 있습니다.</li>
</ul>

<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예</h5>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">my_string</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">"3 + 4"</td>
<td style="user-select: auto;">7</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto;">

<h5 style="user-select: auto;">입출력 예 설명</h5>

<p style="user-select: auto;">입출력 예 #1</p>

<ul style="user-select: auto;">
<li style="user-select: auto;">3 + 4 = 7을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges