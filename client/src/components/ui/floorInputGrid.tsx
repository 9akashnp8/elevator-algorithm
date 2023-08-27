import {
    Card,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"

type Props = {
    numberOfFloors: number
}

export default function FloorInputGrid({ numberOfFloors }: Props) {
    return (
        <div className="grid grid-cols-3 gap-y-5 justify-items-center">
            {[...Array(numberOfFloors)].map((_, i) =>
                <Card>
                    <Button size={"lg"}>
                        {i}
                    </Button>
                </Card>
            )}
        </div>
    )
}