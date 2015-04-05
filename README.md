This is a simple script to upload a file to AWS S3

To use, create a file called pytos3.conf and put your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.

Exemple:

`[credentials]` <br>
`AWS_ACCESS_KEY_ID=HUEHEUHEUEHUHEUHUEHEUHE` <br>
`AWS_SECRET_ACCESS_KEY=AHUAHAUHAUHAUAHUAHHUA` <br>

After that you need to use this format to send your file to a previously created S3 bucket:

`pytos3.py <FILE_PATH> <S3-BUCKET>`
