import humiocore
import time

humiocore.setup_excellent_logging('INFO')

def fetchLastTransfer():
    client = humiocore.HumioAPI(**humiocore.loadenv())
    repositories = client.repositories()

    start = humiocore.utils.parse_ts('-60m@m')
    end = humiocore.utils.parse_ts('@m')

    humioQuery = ('@source = "/var/log/nettbank-pm-betaling/application/trace/tracelog.sb1json" "OpenBankingBetalingResource" "instructionId" '
                '| parseJson(payload) '
                '| regex("(?<from_account_number_prefix>^[0-9]{4})", field=fromAccountNumber) '
                '| regex("(?<to_account_number_prefix>^[0-9]{4})", field=toAccountNumber) '
                '| lookup("from-banks.csv", on=[from_account_number_prefix]) '
                '| lookup("all-to-banks.csv", on=[to_account_number_prefix]) '
                '| format("%d", field=amount, as=amount) '
                '| select([amount, timestamp]) '
                '| tail(1)')
 
    results = client.streaming_search(query=humioQuery, repos=["nettbank-pm-betaling"], start=start, end=end)

    return results

lastResult = next(fetchLastTransfer())

print(lastResult)

while True:
    current = next(fetchLastTransfer())
    if  len(current) != 0 and current["timestamp"] != lastResult["timestamp"]:
        lastResult = current
        print(lastResult["amount"])

    time.sleep(60)
