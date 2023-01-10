# [Silver III] 퇴사 - 14501 

[문제 링크](https://www.acmicpc.net/problem/14501) 

### 성능 요약

메모리: 30616 KB, 시간: 40 ms

### 분류

브루트포스 알고리즘(bruteforcing), 다이나믹 프로그래밍(dp)

### 문제 설명

<p style="user-select: auto;">상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.</p>

<p style="user-select: auto;">오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.</p>

<p style="user-select: auto;">백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.</p>

<p style="user-select: auto;">각각의 상담은 상담을 완료하는데 걸리는 기간 T<sub style="user-select: auto;">i</sub>와 상담을 했을 때 받을 수 있는 금액 P<sub style="user-select: auto;">i</sub>로 이루어져 있다.</p>

<p style="user-select: auto;">N = 7인 경우에 다음과 같은 상담 일정표를 보자.</p>

<table class="table table-bordered" style="user-select: auto;">
	<thead style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;"> </th>
			<th style="user-select: auto;">1일</th>
			<th style="user-select: auto;">2일</th>
			<th style="user-select: auto;">3일</th>
			<th style="user-select: auto;">4일</th>
			<th style="user-select: auto;">5일</th>
			<th style="user-select: auto;">6일</th>
			<th style="user-select: auto;">7일</th>
		</tr>
	</thead>
	<tbody style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;">T<sub style="user-select: auto;">i</sub></th>
			<td style="user-select: auto;">3</td>
			<td style="user-select: auto;">5</td>
			<td style="user-select: auto;">1</td>
			<td style="user-select: auto;">1</td>
			<td style="user-select: auto;">2</td>
			<td style="user-select: auto;">4</td>
			<td style="user-select: auto;">2</td>
		</tr>
		<tr style="user-select: auto;">
			<th style="user-select: auto;">P<sub style="user-select: auto;">i</sub></th>
			<td style="user-select: auto;">10</td>
			<td style="user-select: auto;">20</td>
			<td style="user-select: auto;">10</td>
			<td style="user-select: auto;">20</td>
			<td style="user-select: auto;">15</td>
			<td style="user-select: auto;">40</td>
			<td style="user-select: auto;">200</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto;">1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.</p>

<p style="user-select: auto;">상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.</p>

<p style="user-select: auto;">또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.</p>

<p style="user-select: auto;">퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.</p>

<p style="user-select: auto;">상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p style="user-select: auto;">첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.</p>

<p style="user-select: auto;">둘째 줄부터 N개의 줄에 T<sub style="user-select: auto;">i</sub>와 P<sub style="user-select: auto;">i</sub>가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ T<sub style="user-select: auto;">i</sub> ≤ 5, 1 ≤ P<sub style="user-select: auto;">i</sub> ≤ 1,000)</p>

### 출력 

 <p style="user-select: auto;">첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.</p>

