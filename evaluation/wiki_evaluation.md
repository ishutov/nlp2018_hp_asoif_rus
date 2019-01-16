## Wikipedia pretrained

**Analogies evaluation**
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

|                        |         |   **SECTIONS**     |         |        |         |        
|---------------------------------|---------|--------|---------|--------|----------|
|**Model**| firstname-lastname|child-father | husband-wife|name-species|**total**|
wiki.ru.vec              | 12.5 | 0.0 | 0.0 | 0.0 | **3.41** 
</td><td>

|                        |         |   **SECTIONS**     |         |        |         |       | 
|---------------------------------|---------|--------|---------|------------------|----------|----------|
|**Model**| firstname-lastname|child-father | husband-wife|geo-name-location|houses-seats|**total**|
 wiki.ru.vec              | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **0.0**
</td></tr> </table> 

\
**Doesn't match evaluation**
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

|                        |         |   **SECTIONS**     |         |        |         |        
|---------------------------------|---------|--------|---------|--------|----------|
|**Model**| family-members|Gryffindor-members | magic-creatures|professors|**total**|
 wiki.ru.vec              | 25.45 | 25.0 | 28.29 | 25.0 | **26.79** 
 </td><td>

|                        |         |   **SECTIONS**     |         |        |         |        
|---------------------------------|---------|--------|---------|--------|----------|
|**Model**| family-siblings|names-of-houses | Stark clan|free cities|**total**|
wiki.ru.vec              | 25.0 | 25.0 | 25.0 | 25.0 | **25.0**
</td></tr> </table> 

## ruwikiruscorpora

**Analogies evaluation**
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

|                        |         |   **SECTIONS**     |         |        |         |        
|---------------------------------|---------|--------|---------|--------|----------|
|**Model**| firstname-lastname|child-father | husband-wife|name-species|**total**|
ruwikiruscorpora_upos_skipgram_300_2_2018              | 0.0 | 0.0 | 0.0 | 0.0 | **0.0** 
</td><td>

|                        |         |   **SECTIONS**     |         |        |         |       | 
|---------------------------------|---------|--------|---------|------------------|----------|----------|
|**Model**| firstname-lastname|child-father | husband-wife|geo-name-location|houses-seats|**total**|
 ruwikiruscorpora_upos_skipgram_300_2_2018              | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **0.0**
</td></tr> </table> 

\
**Doesn't match evaluation**
<table>
<tr><th>HP</th><th>ASOIF</th></tr>
<tr><td>

|                        |         |   **SECTIONS**     |         |        |         |        
|---------------------------------|---------|--------|---------|--------|----------|
|**Model**| family-members|Gryffindor-members | magic-creatures|professors|**total**|
 ruwikiruscorpora_upos_skipgram_300_2_2018              | 0.0 | 0.0 | 0.0 | 0.0 | **0.0** 
 </td><td>

|                        |         |   **SECTIONS**     |         |        |         |        
|---------------------------------|---------|--------|---------|--------|----------|
|**Model**| family-siblings|names-of-houses | Stark clan|free cities|**total**|
ruwikiruscorpora_upos_skipgram_300_2_2018              | 0.0 | 0.0 | 0.0 | 0.0 | **0.0**
</td></tr> </table> 
