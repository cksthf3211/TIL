# Git mirror
- clone을 하게 되면 커밋 내역이 없음(껍데기만 남음)
- A 저장소 (1번 개발자)에서 B 저장소(2번 개발자) .

```bash
새로운 저장소 생성
폴더 생성 후 진입
git clone --mirror {1번 개발자 페어 프로그래밍 저장소 주소}
cd {1번개발자의저장소이름}
git remote set-url --push origin {2번 개발자의 새롭게 생성한 저장소 주소}
git push --mirror
```