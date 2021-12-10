
# [
#     (
#         {
#             (
#                 <
#                     (
#                         ()
#                     )
#                     []
#                  >
#                  [
#                     [
#                         {
#                             []
#                             {
#                                 <
#                                     ()
#                                     <>
#                                  >

#now figure out the logic
# You can keep opening, but once you close you it needs to match most recent opening
# At which point the previous opening passes the check then if it closes you need to look for most recent non-passed opening
{
    (
        [
            (
                <
                    {}
                    [
                        <>
                        []
                    } #CORRUPTED
                >
                {
                    []
                        {
                            [
                                (
                                    <()>