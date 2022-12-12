# [Bronze III] 상금 헌터 - 15953 

[문제 링크](https://www.acmicpc.net/problem/15953) 

### 성능 요약

메모리: 30616 KB, 시간: 168 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p style="user-select: auto;">2017년에 이어, 2018년에도 카카오 코드 페스티벌이 개최된다!</p>

<p style="text-align: center; user-select: auto;"><img alt="" src="" style="user-select: auto;"></p>

<p style="user-select: auto;">카카오 코드 페스티벌에서 빠질 수 없는 것은 바로 상금이다. 2017년에 개최된 제1회 코드 페스티벌에서는, 본선 진출자 100명 중 21명에게 아래와 같은 기준으로 상금을 부여하였다.</p>

<div class="table-responsive" style="user-select: auto;">
<table class="table table-bordered" style="user-select: auto;">
	<thead style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;">순위</th>
			<th style="user-select: auto;">상금</th>
			<th style="user-select: auto;">인원</th>
		</tr>
	</thead>
	<tbody style="user-select: auto;">
		<tr style="user-select: auto;">
			<td style="user-select: auto;">1등</td>
			<td style="user-select: auto;">500만원</td>
			<td style="user-select: auto;">1명</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">2등</td>
			<td style="user-select: auto;">300만원</td>
			<td style="user-select: auto;">2명</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">3등</td>
			<td style="user-select: auto;">200만원</td>
			<td style="user-select: auto;">3명</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">4등</td>
			<td style="user-select: auto;">50만원</td>
			<td style="user-select: auto;">4명</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">5등</td>
			<td style="user-select: auto;">30만원</td>
			<td style="user-select: auto;">5명</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">6등</td>
			<td style="user-select: auto;">10만원</td>
			<td style="user-select: auto;">6명</td>
		</tr>
	</tbody>
</table>
</div>

<p style="user-select: auto;">2018년에 개최될 제2회 코드 페스티벌에서는 상금의 규모가 확대되어, 본선 진출자 64명 중 31명에게 아래와 같은 기준으로 상금을 부여할 예정이다.</p>

<div class="table-responsive" style="user-select: auto;">
<table class="table table-bordered" style="user-select: auto;">
	<thead style="user-select: auto;">
		<tr style="user-select: auto;">
			<th style="user-select: auto;">순위</th>
			<th style="user-select: auto;">상금</th>
			<th style="user-select: auto;">인원</th>
		</tr>
	</thead>
	<tbody style="user-select: auto;">
		<tr style="user-select: auto;">
			<td style="user-select: auto;">1등</td>
			<td style="user-select: auto;">512만원</td>
			<td style="user-select: auto;">1명</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">2등</td>
			<td style="user-select: auto;">256만원</td>
			<td style="user-select: auto;">2명</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">3등</td>
			<td style="user-select: auto;">128만원</td>
			<td style="user-select: auto;">4명</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">4등</td>
			<td style="user-select: auto;">64만원</td>
			<td style="user-select: auto;">8명</td>
		</tr>
		<tr style="user-select: auto;">
			<td style="user-select: auto;">5등</td>
			<td style="user-select: auto;">32만원</td>
			<td style="user-select: auto;">16명</td>
		</tr>
	</tbody>
</table>
</div>

<p style="text-align: center; user-select: auto;"><img alt="" src="" style="user-select: auto;"></p>

<p style="user-select: auto;">제이지는 자신이 코드 페스티벌에 출전하여 받을 수 있을 상금이 얼마인지 궁금해졌다. 그는 자신이 두 번의 코드 페스티벌 본선 대회에서 얻을 수 있을 총 상금이 얼마인지 알아보기 위해, 상상력을 발휘하여 아래와 같은 가정을 하였다.</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;">
	<p style="user-select: auto;">제1회 코드 페스티벌 본선에 진출하여 <em style="user-select: auto;">a</em>등(1 ≤ <em style="user-select: auto;">a</em> ≤ 100)등을 하였다. 단, 진출하지 못했다면 <em style="user-select: auto;">a</em> = 0으로 둔다.</p>
	</li>
	<li style="user-select: auto;">
	<p style="user-select: auto;">제2회 코드 페스티벌 본선에 진출하여 <em style="user-select: auto;">b</em>등(1 ≤ <em style="user-select: auto;">b</em> ≤ 64)등을 할 것이다. 단, 진출하지 못했다면 <em style="user-select: auto;">b</em> = 0으로 둔다.</p>
	</li>
</ul>

<p style="user-select: auto;">제이지는 이러한 가정에 따라, 자신이 받을 수 있는 총 상금이 얼마인지를 알고 싶어한다.</p>

### 입력 

 <p style="user-select: auto;">첫 번째 줄에 제이지가 상상력을 발휘하여 가정한 횟수 <em style="user-select: auto;">T</em>(1 ≤ T ≤ 1,000)가 주어진다.</p>

<p style="user-select: auto;">다음 <em style="user-select: auto;">T</em>개 줄에는 한 줄에 하나씩 제이지가 해본 가정에 대한 정보가 주어진다. 각 줄에는 두 개의 음이 아닌 정수 <em style="user-select: auto;">a</em>(0 ≤ <em style="user-select: auto;">a</em> ≤ 100)와 <em style="user-select: auto;">b</em>(0 ≤ <em style="user-select: auto;">b</em> ≤ 64)가 공백 하나를 사이로 두고 주어진다.</p>

### 출력 

 <p style="user-select: auto;">각 가정이 성립할 때 제이지가 받을 상금을 원 단위의 정수로 한 줄에 하나씩 출력한다. 입력이 들어오는 순서대로 출력해야 한다.</p>

