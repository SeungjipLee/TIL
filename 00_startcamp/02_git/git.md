# GIT 이란...
> 분산 버전 관리 시스템 
>- 코드의 변경 이력을 기록하고 협업을 원할하게 하는 도구
- git의 역할
    - 코드의 버전(히스토리)를 관리
    - 개발되어 온 과정 파악
    - 이전 버전과의 변경 사항 비교
- Git의 3가지 영역
   1. Working Directory : 실제 작업하고 있는 영역
   2. Staging Area : Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
   3. Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역. 모든 버전과 변경 이력이 기록됨

### git 초기화
   ```bash
   $ git init
   ```

- Commit(버전) : 변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다하여 'snapshot'이라고 함

### 상태 확인 명령어
```bash
$ git status
```

### Staging Area에 추가
```bash
$ git add {path}<folder_name>/{file_name}
```

### Repository에 저장하기
```bash
$ git commit -m "commit message"
```

### git 기초 설정
```bash
$ git config --global user.email "edward626kr@naver.com"
$ git config --global user.name "이승집"
```

### commit 기록 확인하기
```bash
$ git log 
```