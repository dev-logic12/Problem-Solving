# [level 0] 부분 문자열 - 181842 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181842) 

### 성능 요약

메모리: 33.6 MB, 시간: 0.04 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 04월 07일 10:09:54

### 문제 설명

<p style="user-select: auto !important;">어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열  "abc"는 문자열 "aabcc"의 부분 문자열입니다. </p>

<p style="user-select: auto !important;">문자열 <code style="user-select: auto !important;">str1</code>과 <code style="user-select: auto !important;">str2</code>가 주어질 때, <code style="user-select: auto !important;">str1</code>이 <code style="user-select: auto !important;">str2</code>의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한 사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">str1</code> ≤ <code style="user-select: auto !important;">str2</code> ≤ 20</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">str1</code>과 <code style="user-select: auto !important;">str2</code>는 영어 소문자로만 이루어져 있습니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">str1</th>
<th style="user-select: auto !important;">str2</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"abc"</td>
<td style="user-select: auto !important;">"aabcc"</td>
<td style="user-select: auto !important;">1</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">"tbt"</td>
<td style="user-select: auto !important;">"tbbttb"</td>
<td style="user-select: auto !important;">0</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">본문과 동일합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">"tbbttb"에는 "tbt"가 없으므로 0을 return합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges