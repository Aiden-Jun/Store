# OOP 과제
# 아래의 내용과 완벽하게 일치할 필요 없습니다
# 적당히 비슷하게 제작해보세요
# oop 폴더 내부의 코드를 다음과 같이 업그레이드 하세요

# 회원가입 창
# 이메일, 비밀번호, 유저 종류(구매자, 판매자)를 입력 받으세요
# 유저의 정보를 csv 파일에 저장해야 합니다
# 우선 중복된 이메일이 저장되어 있는지 확인하세요
# 중복되어 있다면 중복된 이메일이라고 보여주고 다시 이메일, 비밀번호를 입력받으세요
# 중복되어 있지 않다면 유저의 정보를 csv 파일에 저장하고 다시 로그인 창을 보여주세요

# 로그인 창
# 이메일, 비밀번호를 입력 받으세요
# csv 파일에 이메일이 존재하고, 비밀번호가 일치하는 유저가 저장되어 있는지 확인하세요
# 저장되어 있다면 유저의 이름으로 환영한다는 메세지를 출력하고 메인 화면을 보여주세요
# 저장되어 있지 않다면 이메일 혹은 비밀번호가 틀렸습니다 라고 메세지를 출력하고 다시 로그인 화면을 보여주세요

# 메인 화면 창: 구매자
# 메인 화면에서는 항상 구매자의 이름, 이메일, 잔액이 제일 위에 보입니다
# 자신의 카트와 현재 구매 가능한 상품 목록을 전부 다 보여주고, 구매하고 싶은 상품의 아이디를 입력받으세요
# 상품 아이디를 입력하면 해당 상품이 구매되고, 내 카트에 상품이 추가됩니다
# 구매하시겠습니까 or 더 둘러보기 중 하나를 입력받으세요
# 구매하시겠습니까를 선택하는 경우 카트는 비워지고, 돈이 차감됩니다. 구매자는 돈을 벌게 됩니다.
# 이 모든 사건에 대해서 csv 파일에 잘 저장해야 합니다
# 더 둘러보기를 하는 경우 다시 모든 상품의 목록과 카트 상태를 보여주세요


# 메인 화면 창: 판매자
# 메인 화면에서는 항상 판매자의 이름, 이메일, 수입이 제일 위에 보입니다
# 자신의 상품 목록을 전부 보여주고, 추가하고 싶은 상품의 이름, 가격, 콘텐츠를 입력받을 수 있습니다.
# 상품을 등록하면 해당 상품이 등록됩니다
# 이 모든 사건에 대해서 csv 파일에 잘 저장해야 합니다

# 로그아웃
# 메인 화면의 어떤 입력창에서도 exit를 입력하면 로그아웃이 됩니다
# 단 프로그램이 종료되지 않습니다. 다른 유저로 로그인할 수 있게 다시 로그인 화면으로 돌아가주세요
