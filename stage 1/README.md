<h1>Stage 1/6: Checking the data type</h1>
<h5>Description</h5>
<p>You just started sorting out the existing database of the &quot;Easy Rider&quot; bus company. As you take the first look at the data, you realize that it&apos;s not going to be easy.</p>
<p>Sometimes numbers are missing from where they should definitely be. You also noticed that sometimes there are too many or too few characters. Fortunately, there is documentation to help you sort out this mess. However, this documentation is not a hundred percent complete: part of it was torn away when your colleague spilled coffee on it. Let&apos;s see what we can make out.</p>
<p>Here are the documents that you have:&nbsp;<a href="https://stepik.org/media/attachments/lesson/412967/Documentation.jpg" rel="noopener noreferrer nofollow" target="_blank">documentation<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a> and&nbsp;<a href="https://stepik.org/media/attachments/lesson/412967/Diagram_of_the_bus_line.jpg" rel="noopener noreferrer nofollow" target="_blank">diagram of the bus lines<img src="http://localhost:63342/eduResources/icons/com/jetbrains/edu/learning/external_link_arrow@2x_dark.png" border="0" width="14" height="14"></a>.</p>
<h5>Objectives</h5>
<ol>
    <li>The string containing the data in JSON format is passed to standard input.</li>
    <li>Check that the&nbsp;<strong>data types</strong> match<strong>.</strong></li>
    <li>Check that the&nbsp;<strong>required fields</strong> are filled in.</li>
    <li>Display the information about the number of found errors in total and in each field. Keep in mind that there might be no errors at all.</li>
    <li>The output should have the same formatting as shown in the example.</li>
</ol>
<p><br></p>
<div>No need to worry about the format now. Let&apos;s at first just make sure that the fields have the right type and all required ones are filled.</div>
<p><br></p>
<p>If you can&apos;t find the necessary information in the stage description, it can probably be found in the attached documentation.</p>
<p>Note that the type&nbsp;Char&nbsp;is present among the data types.</p>
<h5>Example</h5>
<p>Input:</p>
<pre>[
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 1,
        &quot;stop_name&quot;: &quot;Prospekt Avenue&quot;,
        &quot;next_stop&quot;: 3,
        &quot;stop_type&quot;: &quot;S&quot;,
        &quot;a_time&quot;: 8.12
    },
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 3,
        &quot;stop_name&quot;: &quot;&quot;,
        &quot;next_stop&quot;: 5,
        &quot;stop_type&quot;: &quot;&quot;,
        &quot;a_time&quot;: &quot;08:19&quot;
    },
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: 5,
        &quot;stop_name&quot;: &quot;Fifth Avenue&quot;,
        &quot;next_stop&quot;: 7,
        &quot;stop_type&quot;: &quot;O&quot;,
        &quot;a_time&quot;: &quot;08:25&quot;
    },
    {
        &quot;bus_id&quot;: 128,
        &quot;stop_id&quot;: &quot;7&quot;,
        &quot;stop_name&quot;: &quot;Sesame Street&quot;,
        &quot;next_stop&quot;: 0,
        &quot;stop_type&quot;: &quot;F&quot;,
        &quot;a_time&quot;: &quot;08:37&quot;
    },
    {
        &quot;bus_id&quot;: &quot;&quot;,
        &quot;stop_id&quot;: 2,
        &quot;stop_name&quot;: &quot;Pilotow Street&quot;,
        &quot;next_stop&quot;: 3,
        &quot;stop_type&quot;: &quot;S&quot;,
        &quot;a_time&quot;: &quot;&quot;
    },
    {
        &quot;bus_id&quot;: 256,
        &quot;stop_id&quot;: 3,
        &quot;stop_name&quot;: &quot;Elm Street&quot;,
        &quot;next_stop&quot;: 6,
        &quot;stop_type&quot;: &quot;&quot;,
        &quot;a_time&quot;: &quot;09:45&quot;
    },
    {
        &quot;bus_id&quot;: 256,
        &quot;stop_id&quot;: 6,
        &quot;stop_name&quot;: &quot;Sunset Boulevard&quot;,
        &quot;next_stop&quot;: 7,
        &quot;stop_type&quot;: &quot;&quot;,
        &quot;a_time&quot;: &quot;09:59&quot;
    },
    {
        &quot;bus_id&quot;: 256,
        &quot;stop_id&quot;: 7,
        &quot;stop_name&quot;: &quot;Sesame Street&quot;,
        &quot;next_stop&quot;: &quot;0&quot;,
        &quot;stop_type&quot;: &quot;F&quot;,
        &quot;a_time&quot;: &quot;10:12&quot;
    },
    {
        &quot;bus_id&quot;: 512,
        &quot;stop_id&quot;: 4,
        &quot;stop_name&quot;: &quot;Bourbon Street&quot;,
        &quot;next_stop&quot;: 6,
        &quot;stop_type&quot;: &quot;S&quot;,
        &quot;a_time&quot;: &quot;08:13&quot;
    },
    {
        &quot;bus_id&quot;: &quot;512&quot;,
        &quot;stop_id&quot;: 6,
        &quot;stop_name&quot;: &quot;Sunset Boulevard&quot;,
        &quot;next_stop&quot;: 0,
        &quot;stop_type&quot;: 5,
        &quot;a_time&quot;: &quot;08:16&quot;
    }
]</pre>
<p>Output:</p>
<pre>Type and required field validation: 8 errors
bus_id: 2
stop_id: 1
stop_name: 1
next_stop: 1
stop_type: 1
a_time: 2</pre>
<p><br></p>