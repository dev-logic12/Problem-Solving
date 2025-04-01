# [level 0] 배열의 원소 삭제하기 - 181844 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181844) 

### 성능 요약

메모리: 9.27 MB, 시간: 0.19 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 04월 01일 15:09:25

### 문제 설명

<p style="user-select: auto !important;">정수 배열 <code style="user-select: auto !important;">arr</code>과 <code style="user-select: auto !important;">delete_list</code>가 있습니다. <code style="user-select: auto !important;">arr</code>의 원소 중 <code style="user-select: auto !important;">delete_list</code>의 원소를 모두 삭제하고 남은 원소들은 기존의 <code style="user-select: auto !important;">arr</code>에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.</p>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">제한사항</h5>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 길이 ≤ 100</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">arr</code>의 원소 ≤ 1,000</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">arr</code>의 원소는 모두 서로 다릅니다.</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">delete_list</code>의 길이 ≤ 100</li>
<li style="user-select: auto !important;">1 ≤ <code style="user-select: auto !important;">delete_list</code>의 원소 ≤ 1,000</li>
<li style="user-select: auto !important;"><code style="user-select: auto !important;">delete_list</code>의 원소는 모두 서로 다릅니다.</li>
</ul>

<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예</h5>
<table class="table" style="user-select: auto !important;">
        <thead style="user-select: auto !important;"><tr style="user-select: auto !important;">
<th style="user-select: auto !important;">arr</th>
<th style="user-select: auto !important;">delete_list</th>
<th style="user-select: auto !important;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto !important;"><tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[293, 1000, 395, 678, 94]</td>
<td style="user-select: auto !important;">[94, 777, 104, 1000, 1, 12]</td>
<td style="user-select: auto !important;">[293, 395, 678]</td>
</tr>
<tr style="user-select: auto !important;">
<td style="user-select: auto !important;">[110, 66, 439, 785, 1]</td>
<td style="user-select: auto !important;">[377, 823, 119, 43]</td>
<td style="user-select: auto !important;">[110, 66, 439, 785, 1]</td>
</tr>
</tbody>
      </table>
<hr style="user-select: auto !important;">

<h5 style="user-select: auto !important;">입출력 예 설명</h5>

<p style="user-select: auto !important;">입출력 예 #1</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 1번의 <code style="user-select: auto !important;">arr</code>의 원소 중 1000과 94가 <code style="user-select: auto !important;">delete_list</code>에 있으므로 이 두 원소를 삭제한 [293, 395, 678]을 return 합니다.</li>
</ul>

<p style="user-select: auto !important;">입출력 예 #2</p>

<ul style="user-select: auto !important;">
<li style="user-select: auto !important;">예제 2번의 <code style="user-select: auto !important;">arr</code>의 원소 중 <code style="user-select: auto !important;">delete_list</code>에 있는 원소는 없습니다. 따라서 <code style="user-select: auto !important;">arr</code> 그대로인 [110, 66, 439, 785, 1]을 return 합니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges