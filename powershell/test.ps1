$path = "C:\Users\shyju\Desktop\powershell\Book1.csv"
$csv = Import-Csv -path $path

foreach($line in $csv)
{ 
    $properties = $line | Get-Member -MemberType Properties
    for($i=0; $i -lt $properties.Count;$i++)
    {
        $column = $properties[$i]
        $columnvalue = $line | Select -ExpandProperty $column.Name

        # doSomething $column.Name $columnvalue 
        # doSomething $i $columnvalue 
    }
} 
