Sub StockSummary()

Dim ws As Worksheet

For Each ws In Worksheets

    ' Declare variables
    Dim LastRow As Double
    Dim Ticker As String
    Dim YearlyChange As Variant
    Dim PercentChange As Variant
    Dim StockVolumeTotal As Double
    Dim YearOpen As Variant
    Dim YearClose As Variant
    Dim summaryTableOne As Integer
    Dim summaryTableTwo As Integer
    Dim TickerTrack As String

    ' Find last row, stock volume begins with value of 0, summaryTableRow begins on row 2
    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    StockVolumeTotal = 0
    summaryTableOne = 2
    summaryTableTwo = 2
    TickerTrack = ""
    YearOpen = Cells(2, 3).Value

    ' Create Column Headers
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percent Change"
    ws.Cells(1, 12).Value = "Total Stock Volume"
    
    

    ' Run a loop through the worksheet to find necessary data.
    For i = 2 To LastRow
        
        If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then

            Ticker = ws.Cells(i, 1).Value

            StockVolumeTotal = StockVolumeTotal + ws.Cells(i, 7).Value

            ws.Range("L" & summaryTableOne).Value = StockVolumeTotal

            ws.Range("I" & summaryTableOne).Value = Ticker

            summaryTableOne = summaryTableOne + 1

            StockVolumeTotal = 0



        Else

        StockVolumeTotal = StockVolumeTotal + ws.Cells(i, 7).Value

        End If

        If ws.Cells(i, 1).Value <> ws.Cells(i + 1, 1).Value Then
            YearClose = ws.Cells(i, 6).Value
            
            YearlyChange = YearClose - YearOpen
            PercentChange = YearlyChange / YearOpen

            ws.Cells(summaryTableTwo, 10).Value = YearlyChange
            ws.Cells(summaryTableTwo, 11).Value = PercentChange
            ws.Range("J2:J" & LastRow).NumberFormat = "0.000000000"
            ws.Range("K2:K" & LastRow).NumberFormat = "0.00%"
            
            If ws.Cells(summaryTableTwo, 10).Value >= 0 Then
                ws.Cells(summaryTableTwo, 10).Interior.ColorIndex = 4
            ElseIf ws.Cells(summaryTableTwo, 10).Value < 0 Then
                ws.Cells(summaryTableTwo, 10).Interior.ColorIndex = 3
            End If
            
            summaryTableTwo = summaryTableTwo + 1

        ElseIf ws.Cells(i, 1).Value <> ws.Cells(i - 1, 1).Value Then
            YearOpen = ws.Cells(i, 3).Value

            
        End If

    Next i

    ws.Range("I:L").EntireColumn.AutoFit

   

Next ws

End Sub
