SELECT BS1.*, BS2.zTOT as zTOTP1, Not(BS1.Tm==BS2.Tm) as Tm_Switch
  FROM `Basketball_nScores` as BS1 LEFT JOIN `Basketball_nScores` as BS2 
      WHERE BS1.Year=BS2.Year-1 AND BS1.player=BS2.player
UNION
SELECT *,Null, False
  FROM `Basketball_nScores`
      WHERE Year=2018