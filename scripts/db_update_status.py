# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) Diego Gonzalez-Vidal <diegogonzalezvidal@gmail.com>
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with This program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from obspy.core import UTCDateTime
from pygema.db.ask import select_event_from_database, update_event_status


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

this_event, idxev, events_list = select_event_from_database(UTCDateTime(1970, 1,1), UTCDateTime().now(), table="LOC")

print("")
idxs = range(int(idxev)-3, int(idxev)+3) 
for idx in idxs:
  try:
    event = events_list[idx]
    count = idx + 1
    if events_list[idx][0] == this_event[0]:
      if event[8] == 'manual':
        pattern = " --> [%i] %s    %.4f %.4f   %.2f km Ml=%.1f  n=%i gap=%.1f rms=%.4f \x1b[0;32;40m %s \x1b[0m " % (count, event[0].strftime("%Y-%m-%d %H:%M:%S"), event[1], event[2], event[3], event[4], event[5], event[6], event[7], event[8] )
      elif event[8] == 'confirmed':
        pattern = " --> [%i] %s    %.4f %.4f   %.2f km Ml=%.1f  n=%i gap=%.1f rms=%.4f \x1b[0;33;40m %s \x1b[0m " % (count, event[0].strftime("%Y-%m-%d %H:%M:%S"), event[1], event[2], event[3], event[4], event[5], event[6], event[7], event[8] )
      elif event[8] == 'automatic':
        pattern = " --> [%i] %s    %.4f %.4f   %.2f km Ml=%.1f  n=%i gap=%.1f rms=%.4f \x1b[0;31;40m %s \x1b[0m " % (count, event[0].strftime("%Y-%m-%d %H:%M:%S"), event[1], event[2], event[3], event[4], event[5], event[6], event[7], event[8] )
    else:
      if event[8] == 'manual':
        pattern = "     [%i] %s    %.4f %.4f   %.2f km Ml=%.1f  n=%i gap=%.1f rms=%.4f \x1b[0;32;40m %s \x1b[0m " % (count, event[0].strftime("%Y-%m-%d %H:%M:%S"), event[1], event[2], event[3], event[4], event[5], event[6], event[7], event[8] )
      elif event[8] == 'confirmed':
        pattern = "     [%i] %s    %.4f %.4f   %.2f km Ml=%.1f  n=%i gap=%.1f rms=%.4f \x1b[0;33;40m %s \x1b[0m " % (count, event[0].strftime("%Y-%m-%d %H:%M:%S"), event[1], event[2], event[3], event[4], event[5], event[6], event[7], event[8] )
      elif event[8] == 'automatic':
        pattern = "     [%i] %s    %.4f %.4f   %.2f km Ml=%.1f  n=%i gap=%.1f rms=%.4f \x1b[0;31;40m %s \x1b[0m " % (count, event[0].strftime("%Y-%m-%d %H:%M:%S"), event[1], event[2], event[3], event[4], event[5], event[6], event[7], event[8] )

    print(pattern)
  except:
    continue


print("\n[1] automatic\n[2] confirmed\n[3] manual\n[4] rejected")
flag = input("+ What status will you choose? (1, 2, 3, 4): ")
while flag!="1" and flag !="2" and flag !="3" and flag !="4":
  flag = input("+ What status will you choose? (1, 2, 3, 4): ")
  if flag=="yes" or flag =="no":
    break

if flag=="1":
  update_event_status(origin_time=this_event[0], status="automatic", table="LOC")
elif flag=="2":
  update_event_status(origin_time=this_event[0], status="confirmed", table="LOC")
elif flag=="3":
  update_event_status(origin_time=this_event[0], status="manual", table="LOC")
elif flag=="4":
  update_event_status(origin_time=this_event[0], status="rejected", table="LOC")



