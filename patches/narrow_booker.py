"""Cal.diy: show the month and that day's times side by side from 480px up (upstream: 768px).
Run from the cal.diy source root. Every replacement must match exactly once."""
import sys

EDITS = [
    ("packages/features/bookings/Booker/hooks/useBookerLayout.ts",
     'const isMobile = useMediaQuery("(max-width: 768px)");',
     'const isMobile = useMediaQuery("(max-width: 479px)");'),
    ("packages/embeds/embed-core/src/embed-iframe/react-hooks.ts",
     'const isMobile = useMediaQuery("(max-width: 768px)");',
     'const isMobile = useMediaQuery("(max-width: 479px)");'),
    ("packages/features/bookings/Booker/config.ts",
     '"[--booker-timeslots-width:240px] lg:[--booker-timeslots-width:280px]"',
     '"[--booker-timeslots-width:176px] md:[--booker-timeslots-width:240px] lg:[--booker-timeslots-width:280px]"'),
    ("apps/web/modules/bookings/components/Booker.tsx",
     '"h-full overflow-hidden md:w-(--booker-timeslots-width)"',
     '"h-full overflow-hidden border-l w-(--booker-timeslots-width)"'),
    ("apps/web/modules/bookings/components/AvailableTimeSlots.tsx",
     'limitHeight && "no-scrollbar grow overflow-auto md:h-[400px]"',
     'limitHeight && "no-scrollbar grow overflow-auto h-[400px]"'),
]
for path, old, new in EDITS:
    src = open(path, encoding="utf-8").read()
    n = src.count(old)
    if n != 1:
        sys.exit(f"{path}: expected 1 match, found {n}: {old}")
    open(path, "w", encoding="utf-8").write(src.replace(old, new))
    print("patched", path)
