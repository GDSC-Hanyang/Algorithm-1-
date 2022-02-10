# 하샤드 수
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.</p>

<h5>제한 조건</h5>

<ul>
<li><code>x</code>는 1 이상, 10000 이하인 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>arr</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td style="text-align: center">true</td>
</tr>
<tr>
<td>12</td>
<td style="text-align: center">true</td>
</tr>
<tr>
<td>11</td>
<td style="text-align: center">false</td>
</tr>
<tr>
<td>13</td>
<td style="text-align: center">false</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong><br>
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.</p>

<p><strong>입출력 예 #2</strong><br>
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.</p>

<p><strong>입출력 예 #3</strong><br>
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.</p>

<p><strong>입출력 예 #4</strong><br>
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.</p>
</div>
    </div>